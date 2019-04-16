
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
  public show:boolean = false;
  public list: TaskList[] = [
    
  ];
  public loading = false;

  public tasks: Task[] = [];

  public interval;
  public i = 0;

  displayedColumns: string[] = ['id','name','created_at','due_on','status','update','delete'];


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
  
hide(){
  this.show = false;
}
  ngOnDestroy() {
    clearInterval(this.interval);
  }

  getProducts(list: TaskList) {
    this.show = true;
    this.provider.getProducts(list).then(res => {
      this.tasks = res;
    });
  }
  getCategory(){
    this.provider.getCategories().then(res => {
    console.log(res);
    this.list = res;
  });
}
  sendMessageByService() {
    this.provider.sendMessage.emit('This message From Parent Component');
  }


}

 