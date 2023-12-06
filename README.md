# Vendor-rest-api
Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

## API Endpoints
### Vendor
  - POST /api/vendors/ : Create new vendor ( see client/vendor/client_post.py )
  - GET /api/vendors/: List all vendors ( see client/vendor/client_get.py )
  - GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details. ( see client/vendor/client_get_id.py )
  - PUT /api/vendors/{vendor_id}/: Update a vendor's details. ( see client/vendor/client_put.py )
  - DELETE /api/vendors/{vendor_id}/: Delete a vendor. ( see client/vendor/client_delete.py )
  - GET /api/vendors/{vendor_id}/performance/: Retrieves the calculated performance metrics for a specific vendor. ( see client/vendor/client_perform.py )
    
### Purchase Orders
  - POST /api/purchase_orders/: Create a purchase order. ( see client/order/client_post.py )
  - GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor. ( see client/order/client_get.py )
  - GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order. ( see client/order/client_get_id.py )
  - PUT /api/purchase_orders/{po_id}/: Update a purchase order. ( see client/order/client_update.py )
  - DELETE /api/purchase_orders/{po_id}/: Delete a purchase order. ( see client/order/client_delete.py )
  - POST /api/purchase_orders/{po_id}/acknowledge/: Endpont for vendors to acknowledge POs. ( see client/order/client_ack.py )

## API Json sturcture
### Vendor
  Fields for GET,POST,PUT
  - name: CharField - Vendor's name.
  - contact_details: TextField - Contact information of the vendor.
  - address: TextField - Physical address of the vendor.
  - vendor_code: CharField - A unique identifier for the vendor.
  Fields for Get (using '/api/vendors/{vendor_id}/performance/' only)
  - on_time_delivery_rate: FloatField - Tracks the percentage of on-time deliveries.
  - quality_rating_avg: FloatField - Average rating of quality based on purchase orders.
  - average_response_time: FloatField - Average time taken to acknowledge purchase orders.
  - fulfillment_rate: FloatField - Percentage of purchase orders fulfilled successfully.

### Purchase Order
  Fields for GET,POST,PUT
  - po_number: CharField - Unique number identifying the PO.
  - vendor: ForeignKey - Link to the Vendor model.
  - order_date: DateTimeField - Date when the order was placed.
  - delivery_date: DateTimeField - Expected or actual delivery date of the order.
  - items: JSONField - Details of items ordered.
  - quantity: IntegerField - Total quantity of items in the PO.
  - status: CharField - Current status of the PO (e.g., pending, completed, canceled).
  - quality_rating: FloatField - Rating given to the vendor for this PO (nullable).
  - issue_date: DateTimeField - Timestamp when the PO was issued to the vendor.
  Field for POST (only for the vendor to acknowledge)
  - acknowledgment_date: DateTimeField, nullable - Timestamp when the vendor acknowledged the PO.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them:
- Python 3.x
- pip (Python package manager)
- Virtualenv (optional, but recommended)

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. **Clone the Repository**

   ```shell
   git clone https://github.com/Kaustubh05334/vendor-rest-api.git
   cd vendor-rest-api
   ```
2. **Set up virtual environment (recommended)**
   creating virtual environment
   ```shell
   python -m venv env
   ```
   activaing virtual environment
   on Windows
   ```shell
   ./env/Scripts/activate
   ```
   on MacOS or Linux
   ```bash
   source env/bin/activate
   ```
3. **Database Migrations**
   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Create superuser to access admin panel**
   ```shell
   python manage.py createsuperuser
   ```
5. **Run the server on localhost**
   ```shell
   python manage.py runserver
   ```
   this command will run the server on the localhost on port 8000 by default, for running it on specific port
   ```shell
   python manage.py runserver {port}
   ```
Now the server is running and client scripts can be used to make api calls to the server.
