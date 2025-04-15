import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // for *ngIf
import { FormsModule } from '@angular/forms';   // for ngModel, ngForm
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-route-planner',
  standalone: true, // important in standalone Angular
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './route-planner.component.html',
  styleUrls: ['./route-planner.component.css']
})
export class RoutePlannerComponent {
  latitude: number = 33.749;
  longitude: number = -84.388;
  distance: number = 300;

  eta: number | null = null;
  weather: any = null;

  constructor(private http: HttpClient) {}

  getETA() {
    const body = {
      latitude: this.latitude,
      longitude: this.longitude,
      distance_km: this.distance
    };

    this.http.post<any>('http://localhost:8080/api/plan-route', body)
      .subscribe({
        next: (res) => {
          this.eta = res.eta_minutes;
          this.weather = res.weather_used;
        },
        error: (err) => {
          alert('❌ Failed to get ETA');
          console.error(err);
        }
      });
  }
}
