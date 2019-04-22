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
  getDetailedProducts(list: number): Promise<Task> {
    return this.get(`http://localhost:8000/api/task/${list}`, {});
  }
  createTaskList(name: any): Promise<TaskList> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: name
    });
  }
  
  updateTaskList(list: TaskList): Promise<TaskList> {
    return this.put(`http://localhost:8000/api/task_lists/${list.id}/`, {
      name: list.name
    });
  }
  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }

  createTask(name: any,created_at:any,due_on:any,status:any,list:TaskList): Promise<Task> {
    return this.post(`http://localhost:8000/api/task_lists/${list.id}/tasks/`, {
      name: name,
      created_at : created_at,
      due_on:due_on,
      status:status
    });
  }
  updateTask(task: Task){
    return this.put(`http://localhost:8000/api/tasks/${task.id}/`, {
      name: task.name,
      created_at: task.created_at,
      due_on: task.due_on,
      status: task.status
    })
  }

  deleteTask(id: number){
    return this.delet(`http://localhost:8000/api/tasks/${id}/`, {})
  }
}