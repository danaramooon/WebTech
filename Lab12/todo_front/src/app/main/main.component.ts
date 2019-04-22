
import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {ServiceService} from '../services/service.service';
import {TaskList, Task} from '../models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {

  public show:boolean = false;
  public creat:boolean = false;
  public list: TaskList[] = [];
  public loading = false;
  public name: any = '';
  public Tname: any = '';
  public tasks: Task[] = [];
  public status: any = '';
  public created_at: any = '';
  public due_on: any = '';

  displayedColumns: string[] = ['id','name','status'];


  constructor(private provider: ServiceService) { }
  ngOnInit() {
    this.provider.getCategories().then(res => {
      this.list = res;
    });
  }
  
hide(){
  this.show = false;
  this.creat = false;
}

  getProducts(list: TaskList) {
    this.creat = false;
    this.show = true;
    this.provider.getProducts(list).then(res => {
      this.tasks = res;
    });
  }

  updateTaskList(c: TaskList) {
    this.provider.updateTaskList(c).then(res => {
      console.log(c.name + ' updated');
    });
  }

  deleteTaskList(c: TaskList) {
    this.provider.deleteTaskList(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getCategories().then(r => {
        this.list = r;
      });
    });
  }

  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.list.push(res);
      });
    }
  }

  createTask(list:TaskList){
    this.creat = true;
      if (this.Tname !== '' || this.created_at !== '' || this.due_on !== '' || this.status !== '') 
      {
        this.provider.createTask(list,this.Tname,this.created_at,this.due_on,this.status).then(res => {    
          this.tasks.push(res);
          this.Tname = '';
          this.created_at = '';
          this.due_on = '';
          this.status = '';
        });
      }
    }
}

 