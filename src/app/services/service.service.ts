import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {TaskList, Task} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ServiceService extends MainService {

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getCategories(): Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/task_lists/', {});
  }

  getProducts(list: TaskList): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/task_lists/${list.id}/tasks/`, {});
  }

}