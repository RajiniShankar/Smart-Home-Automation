import { Component, OnInit } from '@angular/core';
import axios from 'axios';
import { stringify } from 'querystring';

@Component({
  selector: 'app-list-electronics',
  templateUrl: './list-electronics.component.html',
  styleUrls: ['./list-electronics.component.scss'],
})
export class ListElectronicsComponent implements OnInit {
  electronics;
  baseUrl = 'http://192.168.43.83:8000';

  constructor() { }

  ngOnInit() {
    axios({
      method: 'GET',
      url: this.baseUrl + '/resetPins/'
    }).then(success => {
      axios({
        method: 'GET',
        url: this.baseUrl + '/devices/',
      }).then(res => {
        this.electronics = res.data;
      });
    }).catch(err => {
      console.log(err);
      
    });
  }

  toggle(event: Event) {
    axios({
      method: 'PUT',
      url: this.baseUrl + '/devices/' + event['id'],
      data: {
        id: event['id'],
        name: event['name'],
        status: !event['status']
      }
    }).then(res => {
      event['status'] = !event['status'];
    });
  }

  fetchData() {
    console.log("fetching data");
    
    axios({
      method: 'GET',
      url: this.baseUrl + '/resetPins/'
    }).then(success => {
      axios({
        method: 'GET',
        url: this.baseUrl + '/devices/',
      }).then(res => {
        this.electronics = res.data;
      });
    }).catch(err => {
      console.log(err);
    });
  }
}
