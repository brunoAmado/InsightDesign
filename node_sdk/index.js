/**
 * InsightDesign™ — Universal Node.js / CommonJS SDK (`node_sdk/index.js`)
 * Powered by InsightCore (`insightCoreAI + insightCoreIO`).
 */

class InsightDesignClient {
  constructor(config = {}) {
    this.baseUrl = config.baseUrl || process.env.INSIGHT_DESIGN_URL || 'http://127.0.0.1:4024/api/design';
  }

  async _request(path, method = 'GET', body = null) {
    const opts = {
      method,
      headers: {
        'Content-Type': 'application/json',
        'X-Origin-Platform': 'InsightDesign-NodeSDK'
      }
    };
    if (body !== null) opts.body = JSON.stringify(body);
    const res = await fetch(`${this.baseUrl}${path}`, opts);
    if (!res.ok) throw new Error(`InsightDesign HTTP ${res.status}: ${res.statusText}`);
    return await res.json();
  }

  async getStatus() {
    return await this._request('/status', 'GET');
  }

  async getModes() {
    return await this._request('/modes', 'GET');
  }

  async getBrandDeck(title = 'SetMiddle Pitch Deck', subtitle = 'Open-Source SVG + Slidev') {
    return await this._request(`/brand-deck?title=${encodeURIComponent(title)}&subtitle=${encodeURIComponent(subtitle)}`, 'GET');
  }

  async execute(payload = {}) {
    return await this._request('/execute', 'POST', payload);
  }
}

module.exports = { InsightDesignClient };
