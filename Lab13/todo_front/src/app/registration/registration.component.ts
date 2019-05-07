import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  
  constructor(private auth_:AuthService) { }
  public username: any='';
  public password: any='';
  public email: any='';
  public registration:boolean = false;
  ngOnInit() {
  }
  register(){
    if (this.username != '' && this.password != ''){
      this.auth_.register(this.username, this.password, this.email).then(res => {
        this.username = '';
        this.password = '';
        this.email = '';
      })
    }
  }


}
