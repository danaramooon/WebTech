import { Component, OnInit } from '@angular/core';
import { TaskList,Task } from '../models/models';
import { ServiceService } from '../services/service.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-form-task',
  templateUrl: './form-task.component.html',
  styleUrls: ['./form-task.component.css']
})
export class FormTaskComponent implements OnInit {

  constructor(
    private provider: ServiceService,
    private router: ActivatedRoute) { }
  public list: TaskList[] = [];
  public loading = false;
  public name: any = '';
  public status: any = '';
  public created_at: any = '';
  public due_on: any = '';
  public id: number;
  public tasks: Task[] = [];
  ngOnInit() {
    this.id = parseInt(this.router.snapshot.paramMap.get('id'))

  }
createTask(){
  if (this.name !== '' || this.due_on !== '' || this.status !== '') 
  {
    this.provider.createTask(this.name,this.due_on,this.status,this.id).then(res => {
      this.tasks.push(res);
      console.log(this.tasks);
      this.name = '';
      this.due_on ='';
      this.status = '';
      
      });
    }
  }
}
