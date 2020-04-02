# Flask RESTFull & Swagger & SQLAlchemy Demo
This is a demo project, which contains flask flask-restful flask-sqlalchemy.

## Demo Description:
The demo is a user management micro-service, contains user data model(resource) and 5 APIs:

### 1. Create User
Request URI: **[POST]** /user 
* Description: Create User
* Reqeust Parameters

**Form data**
 
| *PARAMETER* | *TYEP* | *REQUIRE* | *EXAMPLE*        | *DESCRIPTION*            |
| ----------- | ------ | --------- | ---------------- | ------------------------ |
| name        | string | true      | Junyi Song       | user name                |
| email       | string | true      | qsong.vip@qq.com | user email address       |
| tel         | string | true      | 13812345678      | user tel phone No.       |
| password    | string | true      | apassword        | store by secrete         |
| gender      | stirng |           | 1                | 0 null, 1 male, 2 female |
 
Example:

    {
      "nane": "xiaoming",
      "email": "xming@126.com",
      "tel": "13812345678",
      "password": "apassword",
      "gender": "1"
     }

* Response

There are several response status, each status mean a special operation result. 
The mapping of status and operation result as following table:

| *statu code* | *ret_code* | *ret_msg*                                       |
| ------------ | ---------- | ----------------------------------------------- |
| 201          | 20100       | Create user success                            |
| 400          | 40001       | Create user failed, missing required field(s). |
| 406          | 4061       | Create user failed, duplicate username.         |
| 406          | 4062       | Create user failed, duplicate email.            |
| 406          | 4063       | Create user failed, duplicate tel.              |
| 406          | 4064       | Create user failed, invalidate username.        |
| 406          | 4065       | Create user failed, invalidate email.           |
| 407          | 4066       | Create user failed, invalidate tel.             |
| 500          | 5001       | Create user failed, server is crazing.          |

Some Examples as following:

**statue** 200
   
Description: Create user success.

Example:


    {
      "ret_code": "2000",
      "ret_msg": "create user success."
      "user_info": {
                    "id": "1",
                    "name": "xiaoming",
                    "email": "xming@126.com",
                    "tel": "13812345678",
                    "gender": "1",
                    "active": true,
                    "create_time": "2020/04/02 11:04"
      }    
    }   

**statue** 406
   
Description: Create user failed, duplicate username..

Example:

    {
      "ret_code": "4061",
      "ret_msg": "Create user failed, duplicate username." 
    }   


### 2. Delete User
Request URI: **[DELETE]** /user/\<uid> 
* Description: Delete User. It not really delete user object, just inactive it.
* Reqeust Parameters

**URL parametes**

| *PARAMETER* | *TYEP* | *REQUIRE* | *EXAMPLE*        | *DESCRIPTION*            |
| ----------- | ------ | --------- | ---------------- | ------------------------ |
| uid         | string | true      | 1                | user id                  |

Example:

Delete user which id is 1.

[DELETE] http://127.0.0.1/user/1

* Response

There are several response status, each status mean a special operation result. 
The mapping of status and operation result as following table:

| *statu code* | *ret_code* | *ret_msg*                                      |
| ------------ | ---------- | ---------------------------------------------  |
| 200          | 20010       | Delete user success                            |
| 404          | 40400       | Delete user failed, user not exist.            |
| 500          | 50002       | Delete user failed, server is crazing.         |

Some Examples as following:

**statue** 200
   
Description: Delete user success.

Example:


    {
      "ret_code": "2001",
      "ret_msg": "Delete user success."
      "user_info": {
                    "id": "1",
                    "name": "xiaoming",
                    "email": "xming@126.com",
                    "tel": "13812345678",
                    "gender": "1",
                    "active": false,
                    "create_time": "2020/04/02 11:04"
      }    
    }   

**statue** 404
   
Description: Delete user failed, user not exist.

Example:

    {
      "ret_code": "4040",
      "ret_msg": "Delete user failed, user not exist.." 
    }  



### 3. Update User Info.
Request URI: **[PUT]** /user/\<uid> 
* Description: Modify modify several part(s) of user info.
* Reqeust Parameters
  
**URL Parameter(s)**
  
| *PARAMETER* | *TYEP* | *REQUIRE* | *EXAMPLE*        | *DESCRIPTION*            |
| ----------- | ------ | --------- | ---------------- | ------------------------ |
| uid         | string | true      | 1                | user object id           |

**Form data**
 
| *PARAMETER* | *TYEP* | *REQUIRE* | *EXAMPLE*        | *DESCRIPTION*            |
| ----------- | ------ | --------- | ---------------- | ------------------------ |
| name        | string | true      | Junyi Song       | user name                |
| email       | string | true      | qsong.vip@qq.com | user email address       |
| tel         | string | true      | 13812345678      | user tel phone No.       |
| password    | string | true      | apassword        | store by secrete         |
| gender      | stirng |           | 1                | 0 null, 1 male, 2 female |
 
Example:

    {
      "nane": "xiaoming",
      "email": "xming@126.com",
      "tel": "13812345678",
      "password": "apassword",
      "gender": "1"
     }

* Response

There are several response status, each status mean a special operation result. 
The mapping of status and operation result as following table:

| *statu code* | *ret_code* | *ret_msg*                                      |
| ------------ | ---------- | ---------------------------------------------  |
| 200          | 20002      | Update user info success.                      |
| 404          | 40402      | Update user info failed, user not exist.       |
| 406          | 40607      | Update user info failed, duplicate username.   |
| 406          | 40608      | Update user info failed, duplicate email.      |
| 406          | 40609      | Update user info failed, duplicate tel.        |
| 406          | 40610      | Update user info failed, invalidate username.  |
| 406          | 40611      | Update user info failed, invalidate email.     |
| 407          | 40612      | Update user info failed, invalidate tel.       |
| 500          | 50013      | Update user info failed, server is crazing.    |

Some Examples as following:

**statue** 200
   
Description: Update user info success.

Example:

    {
      "ret_code": "2002",
      "ret_msg": "update user success."
      "user_info": {
                    "id": "1",
                    "name": "xiaoming",
                    "email": "xming@126.com",
                    "tel": "13812345678",
                    "gender": "1",
                    "active": true,
                    "create_time": "2020/04/02 11:04"
      }     
    }   

**statue** 406
   
**Description:** Create user failed, duplicate username..

Example:

    {
      "ret_code": "40607",
      "ret_msg": "Update user info failed, duplicate username." 
    }   


### 4. Get User by ID
Request URI: **[GET]** /user/\<uid> 
* Description: Get User by ID.
* Reqeust Parameters

**URL parametes**

| *PARAMETER* | *TYEP* | *REQUIRE* | *EXAMPLE*        | *DESCRIPTION*            |
| ----------- | ------ | --------- | ---------------- | ------------------------ |
| uid         | string | true      | 1                | user id                  |

Example:

Get user which id is 1.

[GET] http://127.0.0.1/user/1

* Response

There are several response status, each status mean a special operation result. 
The mapping of status and operation result as following table:

| *statu code* | *ret_code* | *ret_msg*                                  |
| ------------ | ---------- | -----------------------------------------  |
| 200          | 20030      | Get user success                           |
| 404          | 40403      | Get user failed, user not exist.           |
| 500          | 50003      | Get user failed, server is crazing.        |

Some Examples as following:

**statue** 200
   
Description: Get user success.

Example:


    {
      "ret_code": "2003",
      "ret_msg": "Get user success."
      "user_info": {
                    "id": "1",
                    "name": "xiaoming",
                    "email": "xming@126.com",
                    "tel": "13812345678",
                    "gender": "1",
                    "active": true,
                    "create_time": "2020/04/02 11:04"
      }    
    }   

**statue** 404
   
Description: Get user failed, user not exist.

Example:

    {
      "ret_code": "40403",
      "ret_msg": "Get user failed, user not exist.." 
    }  


### 5. Search Users
Request URI: **[POST]** /users
* Description: Create User
* Reqeust Parameters

**URL Parameters**
 
| *PARAMETER* | *TYEP* | *REQUIRE* | *EXAMPLE*        | *DESCRIPTION*                   |
| ----------- | ------ | --------- | ---------------- | ------------------------------- |
| name        | string | true      | Junyi Song       | user name                       |
| email       | string | true      | qsong.vip@qq.com | user email address              |
| tel         | string | true      | 13812345678      | user tel phone No.              |
| gender      | stirng |           | 1                | 0 null, 1 male, 2 female, 3 all |
 
Example:

    {
      "nane": "xiaoming",
      "email": "xming@126.com",
      "tel": "13812345678",
      "password": "apassword",
      "gender": "1"
     }

* Response

There are several response status, each status mean a special operation result. 
The mapping of status and operation result as following table:

| *statu code* | *ret_code* | *ret_msg*                                      |
| ------------ | ---------- | ---------------------------------------------- |
| 200          | 20004      | Search user success                            |
| 500          | 50004      | Search user failed, server is crazing.         |

Some Examples as following:

**statue** 200
   
Description: Create user success.

Example:


    {
      "ret_code": "20004",
      "ret_msg": "create user success."
      "users_info": [
                     {
                      "id": "1",
                      "name": "xiaoming",
                      "email": "xming@126.com",
                      "tel": "13812345678",
                      "gender": "1",
                      "active": true,
                      "create_time": "2020/04/02 11:04"
                    },
                    {
                      "id": "2",
                      "name": "xiaohong",
                      "email": "xhong@126.com",
                      "tel": "13812345679",
                      "gender": "2",
                      "active": true,
                      "create_time": "2020/04/02 14:03"
                    }
      ]
                       
    }   

**statue** 500
   
Description: Create user failed, duplicate username..

Example:

    {
      "ret_code": "5004",
      "ret_msg": "Search user failed, server crazing." 
    }   

## User Data Model:
User data is defined in mysql database. the data table 'tb_user' as following:

| *column_name* | *column_type* | *limitation*    | *extra*        | *comment*                   |
| --------------| ------------- | --------------- | -------------- | --------------------------- |
| id            | int           | primary_key     | auto_increment | user id                     |
| name          | varchar(20)   | not null        |                | user name                   |
| email         | varchar(20)   | not null unique |                | user email address          |
| tel           | varchar(11)   | not null unique |                | user tel phone No.          |
| password      | varchar(20)   | not null        |                | password in secrete         |
| gender        | varchar(1)    |                 | default 0      | 0 null, 1 male, 2 female    |
| active        | boolean       |                 | default true   | true:active, false:inactive |