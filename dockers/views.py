import pandas as pd
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect, render
from django.db.models import Prefetch
from .forms import UploadFileForm, DocketEntryForm
from .models import Docket,Supplier, PurchaseOrder, DocketEntry

class FileUploadView(TemplateView):
    template_name = 'upload_report.html'  # Specify the path to your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UploadFileForm()  # Pass an instance of the form to the template
        return context

    def handle_supplier_purchase_order(self, supplier_name, purchase_order_number):
        supplier, created = Supplier.objects.get_or_create(name=supplier_name)
        purchase_order, created = PurchaseOrder.objects.get_or_create(
            supplier=supplier,
            number=purchase_order_number,
            defaults={'description': 'Default Description'}  # Provide a default description if necessary
        )
        return supplier, purchase_order

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the uploaded files here (save them, process them, etc.)
            # Access the files using form.cleaned_data['file_field']
            Docket.objects.all().delete()
            DocketEntry.objects.all().delete()
            uploaded_file = request.FILES['file']

            if uploaded_file.name.endswith('.xls') or uploaded_file.name.endswith('.xlsx'):
                # Read the Excel file using pandas
                df = pd.read_excel(uploaded_file)
                df = df.ffill()

                # Iterate through DataFrame and save data to Docket model
                for index, row in df.iterrows():
                    supplier_name = row['Supplier']  # Assuming the column name in Excel for supplier
                    purchase_order_number = row[
                        'PO Number']  # Assuming the column name in Excel for purchase order

                    supplier, purchase_order = self.handle_supplier_purchase_order(supplier_name, purchase_order_number)
                    docket = Docket.objects.create(
                        record_type=row['Record Type'],
                        po_number=purchase_order,
                        chg=row['Chg'],
                        com=row['Com'],
                        docket_type=row['Type'],
                        confirmation=row['Conf'],
                        order_date=row['Order Date'],
                        buyer=row['Buyer'],
                        account_number=row['Account Number'],
                        supplier=supplier,
                        currency=row['Curr'],
                        item=row['Item'],
                        commodity_code=row['Commodity Code'],
                        description=row['Description'],
                        quantity=row['Qty'],
                        unit=row['Un'],
                        order_value=row['Order Value'],
                        amount_invoiced=row['Amount Invoiced'],
                        wbs_code=row['WBS Code'],
                        contract=row['Contract'],
                        remarks=row['Remarks']
                    )

                return redirect('docket_list')
        return self.render_to_response(self.get_context_data(form=form))


class DocketListView(ListView):
    model = Docket
    template_name = 'docket_table.html'  # Specify the template name
    context_object_name = 'dockets'
    paginate_by = 50  # Number of items per page

    def get_queryset(self):
        # You can customize the queryset if needed, e.g., ordering
        return Docket.objects.all().order_by('id')


def get_purchase_orders(request):
    supplier_id = request.GET.get('supplier_id')
    purchase_orders = PurchaseOrder.objects.filter(supplier_id=supplier_id)
    data = [{'id': po.id, 'name': po.number} for po in purchase_orders]
    return JsonResponse({'purchase_orders': data})

def create_docket_entry(request):
    if request.method == 'POST':
        form = DocketEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('created_dockets_list')
    else:
        form = DocketEntryForm()

    return render(request, 'create_docket_entry.html', {'form': form})

def get_purchase_order_description(request):
    purchase_order_id = request.GET.get('purchase_order_id')
    try:
        descriptions = Docket.objects.filter(po_number=purchase_order_id).values('description').distinct()
        descriptions_list = [entry['description'] for entry in descriptions]
        if not descriptions_list:
            descriptions_list = ['Description not found']  # Default description if no descriptions found
    except Docket.DoesNotExist:
        descriptions_list = ['Description not found']  # Default description if PO is not found

    return JsonResponse({'descriptions': descriptions_list})

class CreatedDocketsListView(ListView):
    model = DocketEntry
    template_name = 'created_dockets_list.html'  # Specify the template name
    context_object_name = 'created_dockets'

    def get_queryset(self):
        dockets_with_descriptions = Docket.objects.all().only('id', 'description')
        prefetch_dockets = Prefetch('purchase_order__docket_set', queryset=dockets_with_descriptions, to_attr='dockets')

        return DocketEntry.objects.all().prefetch_related(prefetch_dockets).order_by('-id')

