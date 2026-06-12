# Pyuron ライブ CPI 調整 — 左右両対応ビルド (2026-06-12)

## 内容
- Pyuron_R*.uf2   : 右手（Central）— trackball_R + trackball_L(仮想) の CPI 調整
- Pyuron_L*.uf2   : 左手（Peripheral）— trackball_L の CPI 受信・適用
- settings_reset*.uf2 : NVS クリア用（必要時のみ）

## フラッシュ手順
1. settings_reset を R→L の順に焼く（NVS を一度クリアする場合）
2. Pyuron_R を右手に焼く
3. Pyuron_L を左手に焼く

## 機能
Studio の「CPI」タブに 2 つのエントリが表示されます:
  id=0  trackball_R  (右トラボ / 直接 sensor_attr_set)
  id=1  trackball_L_0 (左トラボ / split BLE 転送経由)

スライダーを動かすと両方リアルタイムで反映・NVS 保存されます。

## リポジトリ
- zmk        : yuitumunii/zmk@pyuron+custom-studio+split-cpi
- pmw3610    : yuitumunii/zmk-pmw3610-driver@live-cpi
- config     : yuitumunii/zmk-config-Pyuron@live-cpi (このビルド)
- GHA run ID : 27394476816
