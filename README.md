Name:Bhusal Sakshi Yogesh
Year:T.E.
Dept:Computer Enginnering
Project Name:Waste Management System

Discription:
The Waste Management System is designed to streamline the management of waste collection and disposal operations. Built using Python's http.server module and connected to a MySQL database, this system provides a robust backend solution for managing various aspects of waste management.

Key Features:
Database Integration:

The system connects to a MySQL database to store and retrieve data related to collection schedules, collection logs, and disposal sites.
Tables include schedules, collections, and disposalsites, allowing the management of areas, collection times, and disposal site utilization.
RESTful API Endpoints:

GET /schedules: Retrieves all the waste collection schedules.
GET /collections: Fetches information about the collections, including schedule details.
GET /disposal-sites: Provides data about disposal sites and their current utilization.
POST /add-schedule: Allows for adding new waste collection schedules.
POST /log-collection: Records a collection's status and time.
POST /update-disposal: Updates the utilization statistics of a disposal site.
Data Management:

The system automatically tracks and logs collection activities, allowing for better waste management insights.
It also updates disposal site utilization to help ensure efficient resource usage.
JSON Response:

The system sends JSON responses for all GET and POST requests, providing structured data that's easy to use in web or mobile applications.
Use Case:
The Waste Management System is intended to help waste management agencies automate and track their operations. It can be used for managing schedules, logging collection events, and keeping track of how much each disposal site is utilized. This API is scalable and can be further expanded to accommodate additional functionality, such as integrating notifications, advanced reporting, and data analytics for improved decision-making.

This project provides a flexible and easy-to-deploy solution to manage the lifecycle of waste management processes.
