# Notification System Design

# Stage 1

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




# Stage 2

## Database Selection

For this notification system, I have chosen **MySQL** as the database.

### Why MySQL?

* MySQL is easy to learn and use.
* It stores data in tables, so the notification data can be organized properly.
* It supports SQL queries to insert, update, delete, and retrieve data.
* It is reliable and commonly used for web applications.

---

## Database Schema

The notification details can be stored in a table called **notifications**.

| Column Name | Data Type    | Description                                             |
| ----------- | ------------ | ------------------------------------------------------- |
| id          | VARCHAR(20)  | Stores the unique notification ID                       |
| title       | VARCHAR(100) | Stores the notification title                           |
| message     | TEXT         | Stores the notification message                         |
| category    | VARCHAR(50)  | Stores the notification type (Placement, Event, Result) |
| isRead      | BOOLEAN      | Shows whether the notification is read or not           |
| createdAt   | DATETIME     | Stores the date and time of notification creation       |

---

## Problems When Data Increases

As more notifications are stored in the database, some problems may occur.

* Fetching notifications may become slower.
* Searching for a notification may take more time.
* The database size will increase.
* If many users use the application at the same time, performance may decrease.

---

## Solutions

These problems can be reduced by using the following methods.

* Create indexes on frequently searched columns like `id`.
* Use pagination to load only a few notifications at a time.
* Remove or archive old notifications that are no longer needed.
* Regularly optimize the database.

---

## SQL Queries

### 1. Get All Notifications

**API**

```text
GET /api/notifications
```

**SQL Query**

```sql
SELECT * FROM notifications;
```

---

### 2. Get Notification By ID

**API**

```text
GET /api/notifications/{id}
```

**SQL Query**

```sql
SELECT * FROM notifications
WHERE id = ?;
```

---

### 3. Create Notification

**API**

```text
POST /api/notifications
```

**SQL Query**

```sql
INSERT INTO notifications
(id, title, message, category, isRead, createdAt)
VALUES
(?, ?, ?, ?, FALSE, NOW());
```

---

### 4. Mark Notification as Read

**API**

```text
PATCH /api/notifications/{id}/read
```

**SQL Query**

```sql
UPDATE notifications
SET isRead = TRUE
WHERE id = ?;
```

---

### 5. Mark All Notifications as Read

**API**

```text
PATCH /api/notifications/read-all
```

**SQL Query**

```sql
UPDATE notifications
SET isRead = TRUE;
```

---

### 6. Delete Notification

**API**

```text
DELETE /api/notifications/{id}
```

**SQL Query**

```sql
DELETE FROM notifications
WHERE id = ?;
```

---

## Conclusion

MySQL is a good choice for this notification system because it is simple and suitable for storing structured data. As the number of notifications increases, techniques like indexing, pagination, and database optimization can help improve performance. The SQL queries shown above support the REST APIs designed in Stage 1.


# Stage 3

## Query Review

### Given Query

```sql
SELECT * FROM notifications
WHERE studentID = 1042 AND isRead = false
ORDER BY createdAt DESC;
```

### Is the Query Correct?

Yes. It correctly returns all unread notifications of the student and sorts them by latest notification.

---

## Why is it Slow?

* The table has millions of records.
* If there is no proper index, the database scans many rows before finding the result.

---

## Improvement

Create a composite index on:

```sql
(studentID, isRead, createdAt)
```

This helps the database find the required records much faster.

**Computation Cost**

* Without index: **O(n)**
* With index: **Approximately O(log n)**

---

## Should We Add Indexes on Every Column?

**No.**

Reasons:

* Indexes use extra storage.
* Insert and update operations become slower.
* Only frequently searched columns should be indexed.

---

## SQL Query

Find all students who received **Placement** notifications in the last 7 days.

```sql
SELECT DISTINCT studentID
FROM notifications
WHERE notificationType = 'Placement'
AND createdAt >= NOW() - INTERVAL 7 DAY;
```

---

## Conclusion

Using the right indexes improves query performance. Adding indexes only where needed is better than indexing every column.
