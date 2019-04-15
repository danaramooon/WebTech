    
export interface TaskList {
    id: number;
    name: string;
  }
  
  export interface Task {
    id: number;
    name: string;
    created_at:string;
    due_on:string;
    status:string;
    task_list:number;
  }