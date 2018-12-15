import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent, SafePipe} from './app.component';
import {GraphComponent} from './pythonGraphs/boxplot/graph.component';

@NgModule({
    declarations: [
        AppComponent,
        GraphComponent,
        SafePipe
    ],
    imports: [
        BrowserModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
