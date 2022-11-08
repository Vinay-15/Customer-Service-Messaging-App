# branch-dev
<h1>Customer Service messaging application 👨‍💻</h1>

This is a complete Desktop Application with full-fledged front-end and back-end structure
- The front-end is built using Python GUI module tkinter.
- The back-end is built on Supabase database (based on Postgres) which is accessed using REST APIs.

## <u>**How to run the application 🛠**</u>
- Dowload this repository as a zip file and extract the contents of it.
- If you are a Windows-OS user, you can just run the ( **branch_app.exe** ) file. The application doesn't have any dependencies. All the modules, packages and libraries are installed in the build folder, so please dont move or remove any files from that folder. Also, make sure you have a good internet connection as well.
- If you are a Linux or Mac OS user, please do read the ( **requirements.text** ) file. You can only run the code as .exe applications are not supported in linux or Mac-OS, all the instructions needed for you to run the application are provided in the text file.

## <u>**Application Features 🔰**</u> 
Basic Features
- Displays the messages of customers.
- The application allows us to easily respond to incomming messages from customers.
- The application can also show us the history of our responses.

Additional Features
- Incorporated the Search Bar functionality.
- Also, a way to divide work amongst agents if two or more agents use the application at the same time.

## <u>**The Application Interface📱**</u>
- ## <u>**The Front-end Part**</u>
  So in the front-end part of the application you can see all the customer messages right at one place and reply to them immediately over there itself.
  
  ![image](https://user-images.githubusercontent.com/84071335/200558705-c349b383-d4db-4896-853c-8504ca508daf.png)
  
  > The below image is the UI of the application.
 
  - The Search bar can be used to search over any message in the entire database.
  - The Refresh button displays new unresolved customer queries on the app.
  - Chat History button can be used to look at our response history.

  ![image](https://user-images.githubusercontent.com/84071335/200565567-a72955d9-2b52-4688-b6eb-10cad2f86367.png)
  
  >The below image gets displayed when the chat history button is pressed.
  <br>
- ## <u>**The Back-end Part**</u>
  This is the main and crucial part of the entire application. All the functionality of Buttons, Search bar functionality, messages being viewed on the frontend are being processed in the back-end and then displayed over the application.
  
  - I've hosted my database on Supabase as it can provide a cloud-hosted realtime Database.
  - Supabase is an open-source alternative for the firebase application
  - The database is accessed or modified using REST APIs ( get, post, put and patch methods )
  ``` 
    GET   : The GET method is used to retrieve data from the server. This is a read-only method
    POST  : The POST method sends data to the server and creates a new resource
    PUT   : The PUT method is most often used to update an existing resource
    PATCH : The PATCH method is very similar to the PUT method because it also modifies an existing resource
  ```
  ![image](https://user-images.githubusercontent.com/84071335/200417359-d843ba28-321b-431e-a3b7-57f3ba58443a.png)
  
  > The above image shows us the databse of the application. 

  - The database contains six fields.
  ``` 
    ID          : Primary key ( the index ) 
    User ID     : Contains the user ID of a customer
    Messages    : Contains the messages sent by the customers
    Timestamp   : Conatins the date and time at when the messages have been sent.
    Response    : The responses we provide are filled in this field
    Response ID : The agent ID given to the messages he's currently replying ( helps to manage and divide work amongst other agents ).
  ```

## <u>**FAQs 📖**</u>
1) Why can't I run the application in Mac OS or Linux ?
   - EXE files are not supported in Mac OS and Linux but you can run .exe files on Linux through Wine (a free software).
   
2) How did I implement a scheme to help agents divide work amongst themselves, and to prevent multiple agents working on the same message at once ?
   - When a user runs the application an Authentication ID (random serial number) is generated for the user and the data he is accessing from the batabase is flagged, the "Response ID" field in the database is filled with the users serial number so other users can't access the same data that he's working on.
   - When a new user also runs the application another new random serial number is assigned for him and he can't access the data that has been flagged by the former user he can only access the un-flagged messages.
   - As soon as a user leaves the application his authentication ID is deleted from all the fields in the database.

![Screenshot 2022-11-08 140521](https://user-images.githubusercontent.com/84071335/200517786-04f389fa-a2d1-4b71-8b94-339156d78b0f.png)

   > The above image there are two Authentication IDs generated for two different users. So, based on the ID the messages will be divided between the agents.
