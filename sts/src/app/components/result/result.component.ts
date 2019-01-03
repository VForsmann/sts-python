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
    {question: 'const', value:  9.5521 },
    {question: 'f4_13', value: 1.9377 },
    {question: 'f8', value: 2.4139 },
    {question: 'f9', value: 2.3203 },
    {question: 'f10_1', value: 2.4366 },
    {question: 'f10_2', value: 1.6620 },
    {question: 'f15_8', value: 1.1903 },
    {question: 'f18_2', value: 1.3560 }
  ];
  headElementsKaiser = ['Frage', 'Kaiserkriterium'];
  elementsKaiser = [
    {question: 'f4_12', value:  0.8128 },
    {question: 'f4_13', value: 0.8322 },
    {question: 'f5_7', value: 0.8798 },
    {question: 'f10_1', value: 0.8732 },
    {question: 'f10_2', value: 0.8240 },
    {question: 'f18_7', value: 0.9024 },
    {question: 'f18_2', value: 0.8986 },
    {question: 'f19_8', value: 0.8244 }
  ];
  ngOnInit() {
  }

}
