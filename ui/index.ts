import { LitElement, html, css, nothing } from 'lit';

// Light DOM is deliberate: native controls keep ordinary forms, labels and engine adapters usable.
// The library owns this markup; consumers listen on nativeControl, and own application state.
const paths: Record<string, string> = {
  play: 'm8 4 12 8-12 8Z', pause: 'M8 5v14M16 5v14', reset: 'M3 11a9 9 0 1 1 2.6 6.4M3 4v7h7',
  sand: 'M5 3h14M5 21h14M7 3v4l10 10v4M17 3v4L7 17v4',
  water: 'M12 3s-7 8-7 12a7 7 0 0 0 14 0c0-4-7-12-7-12Z',
  stone: 'm4 8 6-5 8 2 3 10-5 6-11-2Z', erase: 'm3 14 10-11 8 8-9 10H9Zm5-5 8 8M12 21h9',
  github: 'M9 19c-5 2-5-3-7-3m14 6v-4a3.5 3.5 0 0 0-1-3c3-.3 6-1.5 6-6a4.7 4.7 0 0 0-1.3-3.3 4.4 4.4 0 0 0-.1-3.2S17.5 2 15 3.8a13 13 0 0 0-6 0C6.5 2 4.9 2.5 4.9 2.5a4.4 4.4 0 0 0-.1 3.2A4.7 4.7 0 0 0 3.5 9c0 4.5 3 5.7 6 6a3.5 3.5 0 0 0-1 3v4'
};
class NativeControl extends LitElement {
  static properties = { label: {}, controlId: { attribute: 'control-id' }, disabled: { type: Boolean }, icon: {}, variant: {} };
  label = ''; controlId = ''; disabled = false; icon = ''; variant = 'quiet';
  createRenderRoot() { return this; }
  get nativeControl() { return this.querySelector<HTMLButtonElement>('button'); }
  protected glyph() { return this.icon ? html`<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d=${paths[this.icon] || paths.play}></path></svg>` : nothing; }
  render() { return html`<button class="dv-button" type="button" id=${this.controlId || nothing} ?disabled=${this.disabled} data-variant=${this.variant}>${this.glyph()}<span class="button-label">${this.label}</span></button>`; }
}
export class DeliveratorButton extends NativeControl {}
export class DeliveratorIconButton extends NativeControl {
  render() { return html`<button class="dv-button dv-icon" type="button" id=${this.controlId || nothing} ?disabled=${this.disabled} aria-label=${this.label} title=${this.label}>${this.glyph()}<span class="button-label">${this.label}</span></button>`; }
}
/** Legacy/native engine adapter. Does not replace the focused button or own engine state. */
export function setAction(button: HTMLButtonElement, label: string, icon: string) {
  button.setAttribute('aria-label', label); button.title = label;
  const text = button.querySelector('.button-label'); if (text) text.textContent = label;
  const path = button.querySelector('path'); if (path) path.setAttribute('d', paths[icon] || paths.play);
}
export type Choice = { value: string; label: string; icon?: string };
export class DeliveratorChoiceGroup extends LitElement {
  static properties = { label: {}, value: {}, options: { type: Array }, disabled: { type: Boolean }, iconOnly: { type: Boolean, attribute: 'icon-only' } };
  label = ''; value = ''; options: Choice[] = []; disabled = false; iconOnly = false;
  createRenderRoot() { return this; }
  private select(value: string) {
    this.value = value;
    this.dispatchEvent(new CustomEvent('dv-change', { detail: { value }, bubbles: true, composed: true }));
  }
  render() { return html`<div class="dv-choices" role="group" aria-label=${this.label}>${this.options.map(option => html`<button type="button" class="dv-button" ?disabled=${this.disabled} title=${this.iconOnly ? option.label : nothing} aria-pressed=${String(option.value === this.value)} data-value=${option.value} @click=${() => this.select(option.value)}>${option.icon ? html`<svg viewBox="0 0 24 24" aria-hidden="true"><path d=${paths[option.icon] || paths.play}></path></svg>` : nothing}<span class=${this.iconOnly && option.icon ? 'dv-sr-only' : ''}>${option.label}</span></button>`)}</div>`; }
}
let nextId = 0;
export class DeliveratorRange extends LitElement {
  static properties = { label: {}, value: { type: Number }, min: { type: Number }, max: { type: Number }, step: { type: Number }, disabled: { type: Boolean }, controlId: { attribute: 'control-id' }, format: {} };
  label = ''; value = 0; min = 0; max = 1; step = .05; disabled = false; controlId = ''; format = 'percent';
  private fallbackId = `dv-range-${++nextId}`;
  createRenderRoot() { return this; }
  get nativeControl() { return this.querySelector<HTMLInputElement>('input'); }
  private input(event: Event) { this.value = Number((event.target as HTMLInputElement).value); }
  render() {
    const id = this.controlId || this.fallbackId;
    const display = this.format === 'percent' ? `${Math.round(this.value * 100)}%` : String(this.value);
    const fraction = this.max > this.min ? Math.min(1, Math.max(0, (this.value - this.min) / (this.max - this.min))) : 0;
    return html`<label class="dv-range" for=${id}>${this.label}<output id=${`${id}-value`} for=${id}>${display}</output><input id=${id} type="range" min=${this.min} max=${this.max} step=${this.step} .value=${String(this.value)} style=${`--dv-range-fill:${fraction * 100}%`} aria-valuetext=${display} ?disabled=${this.disabled} @input=${this.input}></label>`;
  }
}
export class DeliveratorToolbar extends LitElement {
  static properties = { label: {} }; label = '';
  createRenderRoot() { return this; }
  connectedCallback() { super.connectedCallback(); this.setAttribute('role', 'group'); }
  updated() { this.setAttribute('aria-label', this.label); }
  render() { return nothing; }
}
export class DeliveratorExhibit extends LitElement {
  static properties = { heading: {} }; heading = '';
  static styles = css`
    :host { display:block; border:1px solid var(--dv-rule); border-radius:var(--dv-panel-radius); overflow:hidden; background:var(--dv-surface); color:var(--dv-text); }
    header { padding:20px 24px; border-bottom:1px solid var(--dv-rule); } h2 { margin:0; font:500 24px/1.2 var(--dv-font); letter-spacing:-.025em; }
    .body { display:grid; grid-template-columns:minmax(0, 1.35fr) minmax(240px, 1fr); }
    .stage { min-width:0; padding:24px; } aside { min-width:0; padding:24px; border-left:1px solid var(--dv-rule); font:400 16px/1.6 var(--dv-font); }
    @media(max-width:720px) { .body { grid-template-columns:1fr; } aside { border-left:0; border-top:1px solid var(--dv-rule); } header,.stage,aside { padding:18px; } }
  `;
  render() { return html`<article aria-label=${this.heading}><header><h2>${this.heading}</h2></header><div class="body"><div class="stage"><slot name="stage"></slot></div><aside><slot name="context"></slot></aside></div></article>`; }
}
for (const [name, ctor] of Object.entries({ 'dv-button': DeliveratorButton, 'dv-icon-button': DeliveratorIconButton, 'dv-choice-group': DeliveratorChoiceGroup, 'dv-range': DeliveratorRange, 'dv-toolbar': DeliveratorToolbar, 'dv-exhibit': DeliveratorExhibit })) {
  if (!customElements.get(name)) customElements.define(name, ctor);
}
