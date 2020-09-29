import { Component } from '@angular/core';
// selector 'app-root' is in the html file. Look at what looks like a custom html tag. Compiler takes care of this for us
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'MilkshakeDB';
}
