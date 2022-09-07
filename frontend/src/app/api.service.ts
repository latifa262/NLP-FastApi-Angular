import { HttpClient,HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private _http: HttpClient;
  private _baseUrl: string;

  constructor(http: HttpClient) {
    this._http = http;
    this._baseUrl = "http://127.0.0.1:8000/"
  }

  public prediction(data): Observable<any> {
    let params = new HttpParams()
      .append('data', data)      
    return this._http.post('http://127.0.0.1:8000/prediction',null ,{
      params: params})
  }

}
