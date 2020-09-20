import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PromotionComponent } from './promotion/promotion.component';

const routes: Routes = [
    { path: '', redirectTo: 'promotion', pathMatch: 'full' },
    { path: 'promotion', component: PromotionComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
