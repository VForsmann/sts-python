import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DataUnderstandingComponent } from './data-understanding.component';

describe('DataUnderstandingComponent', () => {
  let component: DataUnderstandingComponent;
  let fixture: ComponentFixture<DataUnderstandingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DataUnderstandingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DataUnderstandingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
