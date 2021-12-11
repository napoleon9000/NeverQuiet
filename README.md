# NeverQuiet
BE for the App NeverQuiet


## API Documentation

Auth related
 - Register `POST` [/]()
 - Login
 - Merge user accounts (if user is logged in) `POST` [/user/merge]()

Feature related
 - Update user preference `POST` [/{uid}/preference]()
   ```json
   {
     "uid": [string],
     "recipe": [
      {
        "type": [string],
        "percentage": [int, 0...100],
      },
      {
        "type": [string],
        "percentage": [int, 0...100],
      }],
   }
    ```
 - Update user info 'POST' [/{uid}/info]()
   ```json
   {
     "uid": [string],
     "data": {
       "name": [string][Optional],
       "email": [string][Optional],
       "age": [string][Optional],
       ...
       }
   }
   ```

 - Get user text `GET` [/{uid}/text]()
 - Update user status `POST` [/{uid}/surrounding]()
   ```json
   {
     "uid": [string],
     "surrounding": {
          "location": [number, number],
      }  
   }
    ```

## Recipe types:
 - Location based results (lbr)
 - Random jokes (rj)
 - Trending memes (tm)