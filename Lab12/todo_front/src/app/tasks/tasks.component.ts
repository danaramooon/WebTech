import { Component, OnInit } from '@angular/core';
import { ServiceService } from '../services/service.service';
import { Task, TaskList } from '../models/models';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {

  public id: number = 0;
  public name : any = '';
  public tasks: Task[] = [];
  public list: TaskList;
  public task: any = {}
  public status: any = '';
  public created_at: any = '';
  public due_on: any = '';

  constructor(
    private provider: ServiceService,
    private router: ActivatedRoute,
    ) { }
  ngOnInit() {
    this.id = parseInt(this.router.snapshot.paramMap.get('id'))

    if(this.id){
      this.provider.getDetailedProducts(this.id).then(res => {
        this.task = res;
      });
    }
  }
  updateTask(task: Task){
    this.provider.updateTask(task).then(res => {
      this.name = '';
      this.created_at = '';
      this.due_on = '';
      this.status = '';
    })
  }
  deleteTask(c: Task) {
    this.provider.deleteTask(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getProducts(this.list).then(r => {
        this.tasks = r;
      });
    });
  }

}
