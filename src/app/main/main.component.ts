
import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {ServiceService} from '../services/service.service';
import {TaskList, Task} from '../models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit,OnDestroy {

  public output = '';
  public stringArray: string[] = ["df",];

  public list: TaskList[] = [
    {
      'id':1,
      'name':"django"
    },
    {
      'id':2,
      'name':"angular"
    },
    {
      'id':3,
      'name':"all together"
    },
  ];
  public loading = false;

  public tasks: Task[] = [
    {
      'id':1,
      'name':"backApi",
      'created_at':"12/04/2019",
      'due_on':'15/04/2019',
      'status':'done',
      'task_list':1
    },
    {
      'id':1,
      'name':"frontCss",
      'created_at':"13/04/2019",
      'due_on':'14/04/2019',
      'status':'not done',
      'task_list':2
    },
    {
      'id':1,
      'name':"todo_list",
      'created_at':"11/04/2019",
      'due_on':'16/04/2019',
      'status':'not done',
      'task_list':3
    },
  ];

  public interval;
  public i = 0;

  displayedColumns: string[] = ['id','name','created_at','due_on','status'];


  constructor(private provider: ServiceService) { }
  ngOnInit() {
    this.interval = setInterval(() => {
      this.i++;
    }, 1000);

    this.provider.getCategories().then(res => {
      this.list = res;
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });
  }
  

  ngOnDestroy() {
    clearInterval(this.interval);
  }

  getProducts(list: Task) {
    this.provider.getProducts(list).then(res => {
      this.tasks = res;
    });
  }

  sendMessageByService() {
    this.provider.sendMessage.emit('This message From Parent Component');
  }


}

 