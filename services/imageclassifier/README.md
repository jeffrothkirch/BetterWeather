API:
====

route: `/`
-----
example: `!curl localhost:8084`


route: `/filter`
----
example: `!curl -F "links=[\"https://img.grouponcdn.com/deal/5EXVDNMDEe1mtyEK6Pgp/ZC-1057x634/v1/c700x420.jpg\", \"http://st.hzcdn.com/fimgs/4d8155e104ef5d51_2301-w500-h666-b0-p0--transitional-bedroom.jpg\"]" localhost:8084/filter`

```
{
  "result": [
    "https://img.grouponcdn.com/deal/5EXVDNMDEe1mtyEK6Pgp/ZC-1057x634/v1/c700x420.jpg"
  ]
}
```

route: `/classify`
----
example: `!curl -F "links=[\"https://img.grouponcdn.com/deal/5EXVDNMDEe1mtyEK6Pgp/ZC-1057x634/v1/c700x420.jpg\", \"http://st.hzcdn.com/fimgs/4d8155e104ef5d51_2301-w500-h666-b0-p0--transitional-bedroom.jpg\"]" localhost:8084/classify`


```
{
  "result": {
    "images": [
      {
        "image": "https://img.grouponcdn.com/deal/5EXVDNMDEe1mtyEK6Pgp/ZC-1057x634/v1/c700x420.jpg",
        "scores": [
          {
            "classifier_id": "Volcano",
            "name": "Volcano",
            "score": 0.963233
          },
          {
            "classifier_id": "Blue",
            "name": "Blue",
            "score": 0.936151
          },
          {
            "classifier_id": "Snowy_Mountains",
            "name": "Snowy_Mountains",
            "score": 0.926351
          },
          {
            "classifier_id": "Blue_Sky",
            "name": "Blue_Sky",
            "score": 0.912697
          },
          {
            "classifier_id": "Camping",
            "name": "Camping",
            "score": 0.909948
          },
          {
            "classifier_id": "Mountains",
            "name": "Mountains",
            "score": 0.904539
          },
          {
            "classifier_id": "Ice_Scene",
            "name": "Ice_Scene",
            "score": 0.884158
          },
          {
            "classifier_id": "Skiing",
            "name": "Skiing",
            "score": 0.867765
          },
          {
            "classifier_id": "Tiger",
            "name": "Tiger",
            "score": 0.861216
          },
          {
            "classifier_id": "Snow_Sport",
            "name": "Snow_Sport",
            "score": 0.846104
          },
          {
            "classifier_id": "Air_Sport",
            "name": "Air_Sport",
            "score": 0.83526
          },
          {
            "classifier_id": "Hang_Gliding",
            "name": "Hang_Gliding",
            "score": 0.818754
          },
          {
            "classifier_id": "Adventure_Sport",
            "name": "Adventure_Sport",
            "score": 0.808106
          },
          {
            "classifier_id": "Winter_Scene",
            "name": "Winter_Scene",
            "score": 0.626099
          },
          {
            "classifier_id": "Hot_Air_Balloon",
            "name": "Hot_Air_Balloon",
            "score": 0.613004
          },
          {
            "classifier_id": "Bicycle",
            "name": "Bicycle",
            "score": 0.511903
          }
        ]
      },
      {
        "image": "http://st.hzcdn.com/fimgs/4d8155e104ef5d51_2301-w500-h666-b0-p0--transitional-bedroom.jpg",
        "scores": [
          {
            "classifier_id": "Stove",
            "name": "Stove",
            "score": 0.923775
          },
          {
            "classifier_id": "Dish_Washer",
            "name": "Dish_Washer",
            "score": 0.890057
          },
          {
            "classifier_id": "Food_Processor",
            "name": "Food_Processor",
            "score": 0.874959
          },
          {
            "classifier_id": "Refrigerator",
            "name": "Refrigerator",
            "score": 0.828033
          },
          {
            "classifier_id": "Tae_Kwando",
            "name": "Tae_Kwando",
            "score": 0.782322
          },
          {
            "classifier_id": "Wedding",
            "name": "Wedding",
            "score": 0.769142
          },
          {
            "classifier_id": "Clubbing",
            "name": "Clubbing",
            "score": 0.749745
          },
          {
            "classifier_id": "Table_Tennis",
            "name": "Table_Tennis",
            "score": 0.61727
          },
          {
            "classifier_id": "Cake",
            "name": "Cake",
            "score": 0.602318
          },
          {
            "classifier_id": "Hotel_Building",
            "name": "Hotel_Building",
            "score": 0.544233
          },
          {
            "classifier_id": "Bedroom",
            "name": "Bedroom",
            "score": 0.509862
          }
        ]
      }
    ]
  }
}
```