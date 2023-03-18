<h1>Production Schedule App</h1>

This is a Django app that provides a simple interface for creating and managing production schedules for machines and events. The app allows users to view and edit schedules, as well as export and import schedules.

All the activities including the bonuses were completed.
<h2>Installation</h2>

1. Clone the repository to your local machine: `https://github.com/smangaliso/production_schedule.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run database migrations: `python manage.py migrate`

<h2>Usage</h2>

<h3>Creating a Production Schedule </h3>

1. Log in to the admin interface: `http://localhost:8000/admin`
2. Click on the "Production Schedules" link
3. Click the "Add Production Schedule" button
4. Select the machine and event from the dropdown menus
5. Enter the start and end times for the schedule (or the start time and duration)
6. Click "Save"

<h3>Viewing the Production Schedule</h3>

1. Log in to the admin interface: `http://localhost:8000/admin`
2. Click on the "Production Schedules" link
3. Click on a schedule to view the details
4. please note the gantt chart will not be available when the Production Schedule is empty.

<h3>Exporting the Production Schedule</h3>

1. in the terminal run: `python manage.py export_schedule`

2. the exported file will be located in `schedule/fixtures/`


<h3>Importing the Production Schedule</h3>

1. in the terminal run: `python manage.py import_schedule .\test.csv`
2. `test.csv` contains dummy data. you can create your own csv but follow the structure.

