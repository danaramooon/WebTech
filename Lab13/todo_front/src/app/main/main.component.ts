
import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {ServiceService} from '../services/service.service';
import {TaskList, Task, IUser, IAuthResponse} from '../models/models';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {

  public show:boolean = false;
  public create_task:boolean = false;
  public current_list:TaskList;
  public list: TaskList[] = [];
  public loading = false;
  public list_name: any = '';
  public name: any = '';
  public Tname: any = '';
  public tasks: Task[] = [];
  public status: any = '';
  public created_at: any = '';
  public due_on: any = '';
  public user : IUser;

  public username: any='';
  public password: any='';
  public email: any='';

  public owner: boolean=false;
  public registration: any='';

  public isLogged = false;

  displayedColumns: string[] = ['id','name','status'];


  constructor(private provider: ServiceService,
    private auth_:AuthService) { }
  ngOnInit() {
    const token = localStorage.getItem("token");

     if (token && this.auth_.isAuthenticated())
     {
      this.isLogged = true;
      this.username = localStorage.getItem('name')
      this.provider.getCategories().then(res => {
        this.list = res;
      })
    }
  }
  
  hide(){
    this.show = false;
    this.create_task = false;
  }
  showForm(){
    this.show = false;
    this.create_task = true;
  }

  getProducts(list: TaskList) {
    this.current_list = list;
    this.create_task = false;
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
    if (this.list_name !== '') {
      this.provider.createTaskList(this.list_name,this.user).then(res => {
        this.list_name = '';
        this.list.push(res);
      });
    }
  }
}

 