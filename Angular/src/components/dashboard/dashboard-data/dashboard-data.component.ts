import { ChangeDetectionStrategy, Component, inject, OnInit } from '@angular/core';
import { Data } from '@angular/router';
import { Observable } from 'rxjs';
import { DataService } from '../../../services';

@Component({
  selector: 'app-dashboard-data',
  standalone: true,
  imports: [],
  templateUrl: './dashboard-data.component.html',
  styleUrl: './dashboard-data.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DashboardDataComponent implements OnInit {
  private dataServices = inject(DataService)
  data$:Observable<Data> = this.dataServices.getData();

  ngOnInit(): void {
    this.data$
  }
}
