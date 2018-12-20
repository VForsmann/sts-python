import {Component, OnInit} from '@angular/core';

@Component({
    selector: 'app-sidebar',
    templateUrl: './sidebar.component.html',
    styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
    underpoints = null;
    actualElem = null;

    constructor() {
    }

    ngOnInit() {
        this.underpoints = document.getElementsByClassName("navPoint");
        this.getActualElement();
        window.onscroll = () => this.getActualElement();
    }

    getActualElement() {
        for (let i = 0; i < this.underpoints.length; i++) {
            if (this.underpoints[i].getBoundingClientRect().y < (window.innerHeight / 2) && this.underpoints[i].getBoundingClientRect().y > 0) {
                this.actualElem = this.underpoints[i];
                break;
            }
        }
    }
}
