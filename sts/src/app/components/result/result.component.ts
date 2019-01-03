import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.scss']
})
export class ResultComponent implements OnInit {

  constructor() { }

  headElements = ['Frage', 'VIF-Wert'];
  elements = [
    {question: 'const', value:  9.552134 },
    {question: 'f4_13', value: 1.937688 },
    {question: 'f8', value: 2.413905 },
    {question: 'f9', value: 2.320327 },
    {question: 'f10_1', value: 2.436579 },
    {question: 'f10_2', value: 1.662007 },
    {question: 'f15_8', value: 1.190337 },
    {question: 'f18_2', value: 1.356053 }
  ];
  headElementsKaiser = ['Frage', 'Kaiserkriterium'];
  elementsKaiser = [
    {question: 'f4_12', value:  0.812848 },
    {question: 'f4_13', value: 0.832165 },
    {question: 'f5_7', value: 0.879840 },
    {question: 'f10_1', value: 0.873172 },
    {question: 'f10_2', value: 0.823980 },
    {question: 'f18_7', value: 0.902452 },
    {question: 'f18_2', value: 0.898619 },
    {question: 'f19_8', value: 0.824405 }
  ];
  ngOnInit() {
  }

}
