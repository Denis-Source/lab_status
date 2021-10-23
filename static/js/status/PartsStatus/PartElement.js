export class PartElement {
    constructor(partName) {
        this.posPhrase = undefined;
        this.negPhrase = undefined;

        this.data = undefined;

        this.phraseElement = $(`#${partName}-card-status`);
        this.titleElement = $(`#${partName}-card-title`);
        this.spinnerElement = $(`#${partName}-spinner`);
    }

    loadingOn() {
        this.phraseElement.addClass("d-none");
        this.spinnerElement.removeClass("d-none");
    }

    loadingOff() {
        this.phraseElement.removeClass("d-none");
        this.spinnerElement.addClass("d-none");
    }

    drawElement(data) {
        this.data = data;
        if (data.status) {
            this.posPhrase = data.phrase_pos;
            this.phraseElement.text(this.posPhrase);

        } else {
            this.negPhrase = data.phrase_neg;
            this.phraseElement.text(this.negPhrase);
        }
        this.titleElement.text(data.name);
        this.loadingOff();
    }

    updateElementStatus(newStatus) {
        this.data.status = newStatus;
        if (newStatus) {
            this.phraseElement.text(this.posPhrase);

        } else {
            this.phraseElement.text(this.negPhrase);
        }
        this.loadingOff();
    }
}