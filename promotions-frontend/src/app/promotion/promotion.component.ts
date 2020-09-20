import { Component, OnInit } from '@angular/core';
import { PromotionService } from 'src/app/promotion.service';
import { Location } from '@angular/common';


@Component({
  selector: 'app-promotion',
  templateUrl: './promotion.component.html',
  styleUrls: ['./promotion.component.css']
})
export class PromotionComponent implements OnInit {
    promotion = {
        code: '',
        first_name: '',
        last_name: '',
        email: '',
    };
    errMsg = [];
    submitted = false;
    message = '';

    constructor(
        private promotionService: PromotionService,
        private location: Location,
    ) { }

    ngOnInit(): void {
    }

    savePromotion(): void {
        const data = {
            code: this.promotion.code,
            first_name: this.promotion.first_name,
            last_name: this.promotion.last_name,
            email: this.promotion.email,
        };
        this.submitted = false;
        this.promotionService.create(data)
            .subscribe(
                response => {
                    this.submitted=true;

                    switch(response.status) {
                        case -1:
                            this.message = "This email address has already been used for a submission in the last 24 hours.  Please try again tomorrow.";
                            break;
                        case 0:
                            this.message = "Sorry, you are not a winner. Click here to enter another code.";
                            break;
                        case 1:
                            this.message = "Congratulations, you have won a $10 voucher. Please use this code WIN2020 to claim your prize";
                            break;
                    }
                    console.log(response);
                },
                error => {
                    this.errMsg = error.error;
                    console.log(error);
                });
    }

    goBack(): void {
        this.submitted = false;
        this.message = '';
        this.promotion = {
            code: '',
            first_name: '',
            last_name: '',
            email: '',
        };

    }
}
