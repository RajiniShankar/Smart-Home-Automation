import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  electronics = [
    {
      "id": "27",
      "name": 'Light',
      "status": false
    },
    {
      "id": "28",
      "name": 'Light 2',
      "status": false
    },
    {
      "id": "29",
      "name": 'Light 3',
      "status": false
    }
  ];
  constructor() {}

}
