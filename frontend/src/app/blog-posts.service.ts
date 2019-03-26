import { Injectable } from '@angular/core';
import { HttpClient} from "@angular/common/http";
import {Observable} from "rxjs/internal/Observable";

@Injectable({
  providedIn: 'root'
})
export class BlogPostsService {

  public get(url: string): Observable<any>{
    return this.hhtpClient.get(url);
  }

  constructor(private hhtpClient: HttpClient) { }
}
