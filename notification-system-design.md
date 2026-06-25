# Notification System Design

## Introduction

This document contains the REST API design for the Campus Notification System. These APIs help students view notifications related to placements, events, and results. Users can also mark notifications as read and delete them if needed. Admin users can create new notifications.

---

## Authentication

All APIs require authentication using a JWT token.

```
Headers
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
Accept: application/json
```

---

## API Endpoints

## 1. Get All Notifications


### Endpoint
```
GET /api/notifications
```


### Headers
```
Authorization: Bearer <JWT_TOKEN>
```

### Request Body
No request body.

### Response
```
{
  "notifications": [
    {
      "id": "N101",
      "title": "Amazon Placement Drive",
      "message": "Online assessment starts tomorrow.",
      "category": "Placement",
      "isRead": false,
      "createdAt": "2026-06-25T10:00:00Z"
    },
    {
      "id": "N102",
      "title": "Tech Fest",
      "message": "Register before Friday.",
      "category": "Event",
      "isRead": true,
      "createdAt": "2026-06-24T02:30:00Z"
    }
  ]
}
```

### Status Code
```
200 OK
```

## 2. Get Notification By ID

### Endpoint
```
GET /api/notifications/{id}
```

### Headers
```
Authorization: Bearer <JWT_TOKEN>
```

### Request Body
No request body.

### Response
```
{
  "id": "N101",
  "title": "Amazon Placement Drive",
  "message": "Online assessment starts tomorrow.",
  "category": "Placement",
  "isRead": false,
  "createdAt": "2026-06-25T10:00:00Z"
}
```

### Status Code
```
200 OK
```

## 3. Mark Notification as Read

### Endpoint
```
PATCH /api/notifications/{id}/read
```

### Headers
```
Authorization: Bearer <JWT_TOKEN>
```

### Request Body
No request body.

### Response
```
{
  "message": "Notification marked as read successfully."
}
```

### Status Code
```
200 OK
```

## 4. Mark All Notifications as Read

### Endpoint
```
PATCH /api/notifications/read-all
```

### Headers
```
Authorization: Bearer <JWT_TOKEN>
```

### Request Body
No request body.

### Response
```
{
  "message": "All notifications marked as read successfully."
}
```

### Status Code
```
200 OK
```

## 5. Delete Notification

### Endpoint
```
DELETE /api/notifications/{id}
```

### Headers
```
Authorization: Bearer <JWT_TOKEN>
```

### Request Body
No request body.

### Response
```
{
  "message": "Notification deleted successfully."
}
```

### Status Code
```
200 OK
```

## 6. Create Notification (Admin)

### Endpoint
```
POST /api/notifications
```

### Headers
```
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

### Request Body
```
{
  "title": "Placement Drive",
  "message": "Amazon hiring starts tomorrow.",
  "category": "Placement"
}
```

### Response
```
{
  "id": "N103",
  "title": "Placement Drive",
  "message": "Amazon hiring starts tomorrow.",
  "category": "Placement",
  "isRead": false,
  "createdAt": "2026-06-25T11:00:00Z"
}
```

### Status Code
```
201 Created
```

---

## Common Status Codes

200 OK - Request completed successfully.

201 Created - A new notification was created successfully.

400 Bad Request - The request contains invalid data.

401 Unauthorized - Authentication token is missing or invalid.

404 Not Found - The requested notification was not found.

500 Internal Server Error - An unexpected server error occurred.

---

## Conclusion

This REST API design provides the basic operations needed for a campus notification system. It allows students to view and manage notifications while allowing administrators to create new notifications. The APIs follow REST principles with clear endpoints, standard HTTP methods, and JSON request and response formats.