# vendor-rest-api
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
