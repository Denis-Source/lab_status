import {StatusElement} from "../StatusElement.js";

export class ActivityFeedElement extends StatusElement {
    constructor(data) {
        super(data);

        this.element = this.drawElement();
        this.div = this.drawElement();
        this.dataElement = undefined;
    }


    drawElement() {
        let icon_color = `text-${this.data.level}`
        return $(
            `
        <div class="activity-item d-flex">
            <div class="activite-label" id="event-${this.data.id}-timestamp" style="width: 125px">
                ${this.generateReadableTime()}
            </div>
            <i class='bi bi-circle-fill activity-badge ${icon_color} align-self-start'></i>
            <div class="activity-content">
                ${this.data.title}
            </div>   
        </div>
        `
        )
    }

    refreshTime() {
        if (!this.dataElement) {
            this.dataElement = $(`#event-${this.data.id}-timestamp`);
        }
        let timeText = super.generateReadableTime();
        this.dataElement.text(timeText);
    }
}
