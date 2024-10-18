import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Data } from '../models/data.model';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private https = inject(HttpClient)
  private apiUrl = 'http://<IP_DE_TU_RASPBERRY_PI>:5000/data';
  getData(): Observable<Data>{
    return this.https.get<Data>(this.apiUrl)
  }
}
