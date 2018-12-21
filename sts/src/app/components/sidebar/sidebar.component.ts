import {Component, OnInit} from '@angular/core';

@Component({
    selector: 'app-sidebar',
    templateUrl: './sidebar.component.html',
    styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
    underpoints = null;
    actualElem = null;
    unterpunktL = "navPoint-l";
    unterpunktSm = "navPoint-sm";

    constructor() {
    }

    ngOnInit() {
        this.underpoints = document.getElementsByClassName(this.unterpunktL);
        this.sortElements();

        this.getActualElement();
        window.onscroll = () => this.getActualElement();
    }

    getActualElement() {
        for (let i = 0; i < this.underpoints.length; i++) {
            if (this.underpoints[i].getBoundingClientRect().y < window.innerHeight && this.underpoints[i].getBoundingClientRect().y >= 0) {
                this.actualElem = this.underpoints[i];
                break;
            }
        }
    }

    sortElements() {
        let newUnderpoints = [];
        for (let i = 0; i < this.underpoints.length; i++) {
            this.underpoints[i].large = true;
            newUnderpoints[newUnderpoints.length] = this.underpoints[i];
            for (let y = 0; y < this.underpoints[i].parentNode.childNodes.length; y++) {
                if (Array.from(this.underpoints[i].parentNode.childNodes[y].classList).includes(this.unterpunktSm)) {
                    newUnderpoints[newUnderpoints.length] = this.underpoints[i].parentNode.childNodes[y];
                }
            }
        }
        this.underpoints = newUnderpoints;
    }

    scroll(navPoint) {
        this.doScrolling(navPoint.getBoundingClientRect().y, 500);
    }

    doScrolling(elementY, duration) {
        let startingY = document.documentElement.scrollTop;
        let diff = elementY;
        let start;

        window.requestAnimationFrame(function step(timestamp) {
            if (!start) start = timestamp;
            let time = timestamp - start;
            let percent = Math.min(time / duration, 1);
            window.scrollTo(0, startingY + diff * percent);

            if (time < duration) {
                window.requestAnimationFrame(step);
            }
        })
    }
}
