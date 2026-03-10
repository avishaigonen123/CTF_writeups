( () => {
    "use strict";
    var e, t = {
        893: (e, t, a) => {
            var r = a(540)
              , o = a(338);
            const n = "http://localhost:4000/i/api/graphql"
              , i = "/operations-console"
              , s = ( () => {
                if ("undefined" == typeof window)
                    return null;
                if (window.__GRAPHQL_ENDPOINT__)
                    return window.__GRAPHQL_ENDPOINT__;
                const e = window.location.hostname;
                if ("localhost" === e || "127.0.0.1" === e)
                    return n;
                const t = ( () => {
                    if ("undefined" == typeof window)
                        return i;
                    if (window.__OPS_API_BASE__)
                        return window.__OPS_API_BASE__;
                    const [,e] = window.location.pathname.split("/");
                    return e ? `/${e}` : i
                }
                )().replace(/\/+$/, "");
                return `${window.location.origin}${t}/i/api/graphql`
            }
            )() || ("undefined" != typeof globalThis && globalThis.__GRAPHQL_ENDPOINT__ ? globalThis.__GRAPHQL_ENDPOINT__ : null) || n
              , l = (e, t) => e.map( (e, a) => String.fromCharCode(e ^ t.charCodeAt(a % t.length))).join("")
              , d = (l([10, 30, 18, 13, 28, 22, 48, 17, 29, 14, 28, 10, 28, 25, 0, 48, 17, 16, 12, 21, 0, 28], "ops"),
            Object.freeze(["use_grafana_user_traffic", "show_log_defects", "use_graphql_as_main_api", "activate_dark_launch", "enable_synthetic_monitoring", "decode_experimental_feed", "allow_device_impersonation", "use_edge_observability", "stream_replay_cache", "toggle_scout_reports", "hydrate_media_panel", "throttle_push_delivery", "mask_personal_identifiers", "enable_cluster_affinity", "record_visibility_stats", "render_compliance_banner", "allow_stage_metrics", "project_zero_day", "mirror_ops_dashboards", "include_network_trace", "vaulted_payloads", "edge_cache_preload", "security_audit_overlay"]),
            ({queryId: e, operationName: t, operationType: a="query"}) => {
                return r = {
                    queryId: e,
                    operationName: t,
                    operationType: a,
                    metadata: {
                        featureSwitches: {},
                        fieldToggles: {}
                    }
                },
                Object.freeze({
                    endpoint: s,
                    operationType: "query",
                    metadata: {
                        featureSwitches: {},
                        fieldToggles: {}
                    },
                    ...r
                });
                var r
            }
            )
              , u = [[181719, "auth.session.boot", d({
                queryId: "auth:login",
                operationName: "Login",
                operationType: "mutation",
                features: "standard",
                toggles: "minimal"
            })], [468776, "user.preference.prompts", d({
                queryId: "pref:prompts",
                operationName: "PromptPreference",
                features: "minimal",
                toggles: "minimal"
            })], [550574, "users.list", d({
                queryId: "users:list",
                operationName: "Users",
                features: "standard",
                toggles: "standard"
            })], [202020, "profile.show", d({
                queryId: "auth:profile",
                operationName: "AccessProfile",
                features: "standard",
                toggles: "standard"
            })], [96417, "timeline.discovery", d({
                queryId: "timeline:discovery",
                operationName: "DiscoveryTimeline",
                features: "extended",
                toggles: "extended"
            })], [333566, "accounts.blocked.log", d({
                queryId: "accounts:blockedLog",
                operationName: "BlockedAccountsLog",
                features: "extended",
                toggles: "extended"
            })], [664827, "audience.certified", d({
                queryId: "audience:certified",
                operationName: "CertifiedAudience",
                features: "extended",
                toggles: "extended"
            })], [820322, "timeline.highlights", d({
                queryId: "timeline:highlights",
                operationName: "HighlightsSidebar",
                features: "extended",
                toggles: "extended"
            })], [793385, "broadcast.query", d({
                queryId: "broadcast:query",
                operationName: "BroadcastQuery",
                features: "extended",
                toggles: "extended"
            })], [386187, "communities.member.typeahead", d({
                queryId: "communities:memberTypeahead",
                operationName: "CommunityMemberTypeahead",
                features: "standard",
                toggles: "standard"
            })], [765001, "communities.user.typeahead", d({
                queryId: "communities:userTypeahead",
                operationName: "CommunityUserTypeahead",
                features: "standard",
                toggles: "standard"
            })], [311808, "timeline.connect", d({
                queryId: "timeline:connect",
                operationName: "ConnectTimeline",
                features: "extended",
                toggles: "extended"
            })], [58749, "conversation.control.change", d({
                queryId: "conversation:controlChange",
                operationName: "ConversationControlChange",
                operationType: "mutation",
                features: "minimal",
                toggles: "minimal"
            })], [259629, "conversation.control.delete", d({
                queryId: "conversation:controlDelete",
                operationName: "ConversationControlDelete",
                operationType: "mutation",
                features: "minimal",
                toggles: "minimal"
            })], [954122, "bookmark.create", d({
                queryId: "bookmark:create",
                operationName: "CreateBookmark",
                operationType: "mutation",
                features: "minimal",
                toggles: "minimal"
            })], [570667, "highlight.create", d({
                queryId: "highlight:create",
                operationName: "CreateHighlight",
                operationType: "mutation",
                features: "minimal",
                toggles: "minimal"
            })], [724, "journal.record", d({
                queryId: "journal:create",
                operationName: "CreateJournal",
                operationType: "mutation",
                features: "extended",
                toggles: "extended"
            })], [419689, "relay.create", d({
                queryId: "relay:create",
                operationName: "CreateRelay",
                operationType: "mutation",
                features: "minimal",
                toggles: "minimal"
            })], [995240, "post.compose", d({
                queryId: "post:create",
                operationName: "CreatePost",
                operationType: "mutation",
                features: "extended",
                toggles: "extended"
            })], [940742, "creator.memberships.timeline", d({
                queryId: "creator:membershipsTimeline",
                operationName: "CreatorMembershipsTimeline",
                features: "extended",
                toggles: "extended"
            })], [874066, "user.bandwidth.read", d({
                queryId: "user:bandwidthRead",
                operationName: "BandwidthMode",
                features: "minimal",
                toggles: "minimal"
            })], [730346, "user.bandwidth.write", d({
                queryId: "user:bandwidthWrite",
                operationName: "BandwidthPreferences",
                operationType: "mutation",
                features: "minimal",
                toggles: "minimal"
            })], [131313, "vault.audit", d({
                queryId: "vault:audit",
                operationName: "VaultAudit",
                features: "standard",
                toggles: "standard"
            })], [141414, "network.health", d({
                queryId: "network:health",
                operationName: "NetworkHealth",
                features: "standard",
                toggles: "minimal"
            })], [151515, "labs.experimental", d({
                queryId: "labs:experimental",
                operationName: "LabsExperimental",
                features: "standard",
                toggles: "standard"
            })], [161616, "labs.sandbox", d({
                queryId: "labs:sandbox",
                operationName: "LabsSandbox",
                features: "minimal",
                toggles: "minimal"
            })], [171717, "integration.notifications", d({
                queryId: "integration:notifications",
                operationName: "IntegrationNotifications",
                features: "standard",
                toggles: "standard"
            })], [181818, "integration.search", d({
                queryId: "integration:search",
                operationName: "IntegrationSearch",
                features: "standard",
                toggles: "minimal"
            })]]
              , c = Object.freeze(u.reduce( (e, [t,a,r]) => (e.modules[t] = r,
            e.keys[a] = t,
            e), {
                modules: Object.create(null),
                keys: Object.create(null)
            }))
              , m = Object.freeze({
                login: c.keys["auth.session.boot"],
                listUsers: c.keys["users.list"],
                profile: c.keys["profile.show"]
            })
              , p = (Object.freeze({
                public: Object.keys(m),
                decoys: Object.keys(c.keys).filter(e => !Object.values(m).includes(c.keys[e]))
            }),
            e => {
                if (!e)
                    return null;
                const t = m[e] || c.keys[e] || c.keys[e.toLowerCase?.()] || e;
                return ("number" == typeof t ? c.modules[t] : c.modules[c.keys[t]]) || null
            }
            );
            Symbol.for(l([0, 0, 0, 65, 17, 29, 14, 28, 10, 28, 25, 0, 65, 24, 26, 1, 4], "ops"));
            var g = a(848);
            const h = ["use_grafana_user_traffic", "show_log_defects", "use_graphql_as_main_api", "activate_dark_launch", "enable_synthetic_monitoring", "decode_experimental_feed", "allow_device_impersonation", "use_edge_observability", "stream_replay_cache", "toggle_scout_reports", "hydrate_media_panel", "throttle_push_delivery", "mask_personal_identifiers", "enable_cluster_affinity", "record_visibility_stats", "show_flag", "render_compliance_banner", "allow_stage_metrics", "try_admin_check", "project_zero_day", "mirror_ops_dashboards", "include_network_trace", "vaulted_payloads", "edge_cache_preload", "security_audit_overlay"]
              , _ = ["withAuxiliaryLabels", "withPayments", "withRichContentState", "withPlainText", "withInsightAnalysis", "withReplyControls"]
              , f = (e, t) => ( (e, t=4) => {
                const a = [...e]
                  , r = Math.max(1, Math.floor(Math.random() * t))
                  , o = [];
                for (; o.length < r && a.length > 0; ) {
                    const e = Math.floor(Math.random() * a.length);
                    o.push(a.splice(e, 1)[0])
                }
                return o
            }
            )(e, t).reduce( (e, t) => (e[t] = !0,
            e), {})
              , y = (e={}) => Object.entries(e || {}).filter( ([,e]) => e).reduce( (e, [t]) => (e[t] = !0,
            e), {})
              , b = function() {
                const [e,t] = (0,
                r.useState)("")
                  , [a,o] = (0,
                r.useState)("")
                  , [n,i] = (0,
                r.useState)(!1)
                  , [l,d] = (0,
                r.useState)("");
                return (0,
                r.useEffect)( () => {
                    document.cookie = "auth_token=; path=/; Max-Age=0; SameSite=Lax"
                }
                , []),
                (0,
                g.jsxs)("div", {
                    className: "app-shell",
                    children: [(0,
                    g.jsxs)("header", {
                        children: [(0,
                        g.jsx)("p", {
                            className: "eyebrow",
                            children: "Secure Area"
                        }), (0,
                        g.jsx)("h1", {
                            children: "Operations Console"
                        }), (0,
                        g.jsx)("p", {
                            className: "subtitle",
                            children: "Authorized personnel only. Credentials are required for access."
                        })]
                    }), (0,
                    g.jsx)("main", {
                        children: (0,
                        g.jsxs)("section", {
                            className: "panel",
                            children: [(0,
                            g.jsxs)("form", {
                                className: n ? "login-form is-loading" : "login-form",
                                onSubmit: async t => {
                                    t.preventDefault(),
                                    i(!0),
                                    d("");
                                    try {
                                        const t = await async function(e, t={}) {
                                            const a = p(e);
                                            if (!a)
                                                throw new Error(`Unknown operation "${e}"`);
                                            const r = new URLSearchParams;
                                            r.set("variables", JSON.stringify(t));
                                            const o = f(h)
                                              , n = f(_)
                                              , i = y({
                                                ...o,
                                                ...a.metadata?.featureSwitches || {}
                                            })
                                              , l = y({
                                                ...n,
                                                ...a.metadata?.fieldToggles || {}
                                            });
                                            r.set("features", JSON.stringify(i)),
                                            r.set("fieldToggles", JSON.stringify(l));
                                            const d = `${a.endpoint || s}/${a.queryId}/${a.operationName}?${r.toString()}`
                                              , u = await fetch(d, {
                                                method: "GET",
                                                headers: {
                                                    Accept: "application/json"
                                                }
                                            })
                                              , c = await u.json();
                                            if (!u.ok || c.errors)
                                                throw new Error(c?.errors?.[0]?.message || c?.message || "Request failed");
                                            return c.data
                                        }("login", {
                                            username: e,
                                            password: a
                                        });
                                        t.login.success || d(t.login.message || "Login failed")
                                    } catch (e) {
                                        d(e.message || "Unable to reach GraphQL API")
                                    } finally {
                                        i(!1)
                                    }
                                }
                                ,
                                children: [(0,
                                g.jsx)("label", {
                                    htmlFor: "username",
                                    children: "Username"
                                }), (0,
                                g.jsx)("input", {
                                    id: "username",
                                    name: "username",
                                    type: "text",
                                    autoComplete: "off",
                                    placeholder: "username",
                                    value: e,
                                    onChange: e => t(e.target.value),
                                    disabled: n
                                }), (0,
                                g.jsx)("label", {
                                    htmlFor: "password",
                                    children: "Password"
                                }), (0,
                                g.jsx)("input", {
                                    id: "password",
                                    name: "password",
                                    type: "password",
                                    placeholder: "••••••••",
                                    value: a,
                                    onChange: e => o(e.target.value),
                                    disabled: n
                                }), (0,
                                g.jsx)("button", {
                                    type: "submit",
                                    disabled: n,
                                    children: n ? "CONTACTING ORACLE…" : "ACCESS TERMINAL"
                                })]
                            }), l ? (0,
                            g.jsx)("p", {
                                className: "error",
                                children: l
                            }) : null]
                        })
                    })]
                })
            };
            (0,
            o.createRoot)(document.getElementById("root")).render((0,
            g.jsx)(r.StrictMode, {
                children: (0,
                g.jsx)(b, {})
            }))
        }
    }, a = {};
    function r(e) {
        var o = a[e];
        if (void 0 !== o)
            return o.exports;
        var n = a[e] = {
            exports: {}
        };
        return t[e](n, n.exports, r),
        n.exports
    }
    r.m = t,
    e = [],
    r.O = (t, a, o, n) => {
        if (!a) {
            var i = 1 / 0;
            for (u = 0; u < e.length; u++) {
                for (var [a,o,n] = e[u], s = !0, l = 0; l < a.length; l++)
                    (!1 & n || i >= n) && Object.keys(r.O).every(e => r.O[e](a[l])) ? a.splice(l--, 1) : (s = !1,
                    n < i && (i = n));
                if (s) {
                    e.splice(u--, 1);
                    var d = o();
                    void 0 !== d && (t = d)
                }
            }
            return t
        }
        n = n || 0;
        for (var u = e.length; u > 0 && e[u - 1][2] > n; u--)
            e[u] = e[u - 1];
        e[u] = [a, o, n]
    }
    ,
    r.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t),
    ( () => {
        var e = {
            792: 0
        };
        r.O.j = t => 0 === e[t];
        var t = (t, a) => {
            var o, n, [i,s,l] = a, d = 0;
            if (i.some(t => 0 !== e[t])) {
                for (o in s)
                    r.o(s, o) && (r.m[o] = s[o]);
                if (l)
                    var u = l(r)
            }
            for (t && t(a); d < i.length; d++)
                n = i[d],
                r.o(e, n) && e[n] && e[n][0](),
                e[n] = 0;
            return r.O(u)
        }
          , a = self.webpackChunkfrontend = self.webpackChunkfrontend || [];
        a.forEach(t.bind(null, 0)),
        a.push = t.bind(null, a.push.bind(a))
    }
    )();
    var o = r.O(void 0, [179], () => r(893));
    o = r.O(o)
}
)();
