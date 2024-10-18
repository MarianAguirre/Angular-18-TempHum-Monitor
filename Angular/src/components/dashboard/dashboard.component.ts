import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { AsyncPipe } from '@angular/common';
import { DashboardDataComponent } from './dashboard-data';
import { Chart } from 'chart.js';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [AsyncPipe],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DashboardComponent implements OnInit {
  chart: any;

  ngOnInit(): void {
      this.createChart();
  }

  createChart() {
    this.chart = new Chart('canvas', {
      type: 'line',
      data: {
        labels: ['Temperature', 'Humidity'],
        datasets: [
          {
            label: 'Sensor Data',
            data: [DashboardDataComponent],
            backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgba(255,99,132,1)', 'rgba(54,162,235,1)'],
            borderWidth: 1,
          },
        ],
      },
    });
  }
}
