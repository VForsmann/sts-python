import {Component, OnInit} from '@angular/core';
import {setContextDirty} from "@angular/core/src/render3/styling";
import {callHooks} from "@angular/core/src/render3/hooks";

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
        this.handleBackupScrolls();
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

    scroll(navPoint: any) {
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

    handleBackupScrolls() {

        let scrollTos = Array.from(document.querySelectorAll('[scrollTo]'));
        scrollTos.forEach((elem) => {
            elem.addEventListener('click', () => {
                let matchedValue = elem.attributes.getNamedItem('scrollTo').value;
                let elemFound = document.getElementById(matchedValue);

                function activeListener() {
                    this.scroll(elem);
                    elemFound.removeEventListener('click', list);
                }

                let list = () => activeListener.call(this);
                try {
                    elemFound.addEventListener('click', list);
                    this.scroll(elemFound);
                } catch (err) {
                    console.warn("Es wurde ein 'scrollTo' Attribut verwendet ohne die ID des zugehörigen Elements korrekt zu setzen.")
                }
            })
        })

    }
}
