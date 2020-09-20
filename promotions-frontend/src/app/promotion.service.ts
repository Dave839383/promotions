import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const baseUrl = 'http://localhost:8000/promotion/';

@Injectable({
  providedIn: 'root'
})
export class PromotionService {

    constructor(private http: HttpClient) { }

    create(data): Observable<any> {
        return this.http.post(baseUrl, data);
    }
}
