import { LitElement, html, css, nothing } from 'lit';
import { unsafeSVG } from 'lit/directives/unsafe-svg.js';
import { icons } from './icons.generated';
export function iconMarkup(name: string) { if (!icons[name]) throw new Error(`Unknown Deliverator icon: ${name}`); return icons[name]; }

// Light DOM is deliberate: native controls keep ordinary forms, labels and engine adapters usable.
// The library owns this markup; consumers listen on nativeControl, and own application state.
class NativeControl extends LitElement {
  static properties = { label: {}, controlId: { attribute: 'control-id' }, disabled: { type: Boolean }, icon: {}, variant: {} };
  label = ''; controlId = ''; disabled = false; icon = ''; variant = 'quiet';
  createRenderRoot() { return this; }
  get nativeControl() { return this.querySelector<HTMLButtonElement>('button'); }
  protected glyph() { return this.icon ? unsafeSVG(iconMarkup(this.icon)) : nothing; }
  render() { return html`<button class="dv-button" type="button" id=${this.controlId || nothing} ?disabled=${this.disabled} data-variant=${this.variant}>${this.glyph()}<span class="button-label">${this.label}</span></button>`; }
}
export class DeliveratorButton extends NativeControl {}
export class DeliveratorIconButton extends NativeControl {
  render() { return html`<button class="dv-button dv-icon" type="button" id=${this.controlId || nothing} ?disabled=${this.disabled} aria-label=${this.label} title=${this.label}>${this.glyph()}<span class="button-label">${this.label}</span></button>`; }
}
/** Legacy/native engine adapter. Does not replace the focused button or own engine state. */
export function setAction(button: HTMLButtonElement, label: string, icon: string) {
  if (button.getAttribute('aria-label') !== label) button.setAttribute('aria-label', label); button.title = label;
  const text = button.querySelector('.button-label'); if (text) text.textContent = label;
  const glyph = button.querySelector('svg');
  if (glyph?.getAttribute('data-dv-icon') !== icon) {
    const template = document.createElement('template'); template.innerHTML = iconMarkup(icon);
    if (glyph) glyph.replaceWith(template.content); else button.prepend(template.content);
  }
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
  render() { return html`<div class="dv-choices" role="group" aria-label=${this.label}>${this.options.map(option => html`<button type="button" class="dv-button" ?disabled=${this.disabled} title=${this.iconOnly ? option.label : nothing} aria-pressed=${String(option.value === this.value)} data-value=${option.value} @click=${() => this.select(option.value)}>${option.icon ? unsafeSVG(iconMarkup(option.icon)) : nothing}<span class=${this.iconOnly && option.icon ? 'dv-sr-only' : ''}>${option.label}</span></button>`)}</div>`; }
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
