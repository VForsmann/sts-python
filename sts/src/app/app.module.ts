import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AppComponent, SafePipe} from './app.component';
import {GraphComponent} from './components/graph/graph.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {IntroductionComponent} from './components/introduction/introduction.component';
import {DataUnderstandingComponent} from './components/data-understanding/data-understanding.component';
import {DataPreparationComponent} from './components/data-preparation/data-preparation.component';
import {RouterModule} from '@angular/router';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { BackupComponent } from './components/backup/backup.component';
import { ResultComponent } from './components/result/result.component';
import { ConclusionComponent } from './components/conclusion/conclusion.component';

@NgModule({
    declarations: [
        AppComponent,
        GraphComponent,
        SafePipe,
        IntroductionComponent,
        DataUnderstandingComponent,
        DataPreparationComponent,
        SidebarComponent,
        BackupComponent,
        ResultComponent,
        ConclusionComponent
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
