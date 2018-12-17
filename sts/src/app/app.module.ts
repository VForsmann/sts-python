import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AppComponent, SafePipe} from './app.component';
import {GraphComponent} from './pythonGraphs/boxplot/graph.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {IntroductionComponent} from './components/introduction/introduction.component';
import {DataUnderstandingComponent} from './components/data-understanding/data-understanding.component';
import {RouterModule} from "@angular/router";

@NgModule({
    declarations: [
        AppComponent,
        GraphComponent,
        SafePipe,
        IntroductionComponent,
        DataUnderstandingComponent
    ],
    imports: [
        BrowserModule,
        NgbModule,
        RouterModule.forRoot([])
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
