import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';



@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent{
  predic: string;
  data: string;
 

  constructor(
    private apiService: ApiService,
  ) {
  }

  public onPredict(): void {
    this.apiService.prediction(this.data).subscribe(
      response => {this.predic = response;
      console.log("done", this.predic);
      });
  }

}