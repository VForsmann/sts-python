import { Component, OnInit, Input, SimpleChanges,} from "@angular/core";

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.scss']
})
export class GraphComponent implements OnInit {
    @Input() data;
    @Input() height;
    @Input() width;
    url: string = "http://localhost:3000/";

    constructor() {
    }
    ngOnInit() {

    }
    ngOnChanges() {
        this.url += this.data;
    }


}