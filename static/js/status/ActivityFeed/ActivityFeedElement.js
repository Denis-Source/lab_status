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
        <div class="activity-item d-flex" id="event-${this.data.id}">
            <div class="activite-label" id="event-${this.data.id}-timestamp" style="width: 125px">
                ${this.generateReadableTime()}
            </div>
            <i class='bi bi-circle-fill activity-badge ${icon_color} align-self-start'></i>
            <div class="activity-content d-flex">
                ${this.data.title}
                <div class="d-none" style="margin-left: 15px" id="video-spinner-${this.data.id}">
                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                    Recording...
                </div>
                <a class="d-none" style="margin-left: 15px" id="video-link-${this.data.id}">
                    Watch Video
                </a>
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

    refreshElementInfo(data) {
        let spinnerSelector = $(`#video-spinner-${this.data.id}`);
        let videoLinkSelector = $(`#video-link-${this.data.id}`);

        if (data.camera_name) {
            if (!data.is_video_recorded && data.camera_name) {
                spinnerSelector.removeClass("d-none");
            } else {
                spinnerSelector.addClass("d-none");
                videoLinkSelector.prop("href", `/events/${this.data.id}`);
                videoLinkSelector.removeClass("d-none")
            }
        }
    }
}
