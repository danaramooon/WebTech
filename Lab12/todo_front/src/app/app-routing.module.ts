import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { TasksComponent } from './tasks/tasks.component';
import { FormTaskComponent } from './form-task/form-task.component';

const routes: Routes = [
  {path: 'task/:id', component: TasksComponent },
  {path: 'task_create/:id', component: FormTaskComponent },
  {path: 'task_list', component: MainComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
